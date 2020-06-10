import os

from my2to3.trace import patch_imports, tracing_functions, apply_fixers
from Products.PythonScripts.PythonScript import PythonScript
from Products.PageTemplates.ZRPythonExpr import PythonExpr
from RestrictedPython import compile_restricted_eval

from . import PatchClass


erp5_products_path = os.path.join(os.path.dirname(__file__), '..', '..')
erp5_products = ['Products.' + p for p in os.listdir(erp5_products_path)
                 if os.path.isdir(os.path.join(erp5_products_path, p))]


# Apply "trace" fixers on the fly
if os.environ.get("MY2TO3_ACTION") == "trace":
  def is_whitelisted(fullname, path):
    return any(fullname.startswith(p) for p in erp5_products)

  # Apply "trace" fixers on the fly, when importing modules
  patch_imports(is_whitelisted)

  # Apply "trace" fixers on the fly, on PythonScript bodies
  # Note: The modifications are not saved (unless it is done explicitly, e.g.
  # the user saves manually).
  class _(PatchClass(PythonScript)):
    ___setstate__ = PythonScript.__setstate__
    def __setstate__(self, state):
      self.___setstate__(state)

      if '_body' in state:
        # Note that self.___setstate__ is called unconditionally a first time,
        # before. The reason is:
        #   We need the file path (i.e. self.get_filepath()). This information
        #   is contained in state['_filepath'], but it is not always the case.
        #   Calling ___setstate__ before makes this information available.
        state['_body'] = apply_fixers(state['_body'], self.get_filepath())
        # This time, it's called to update the body.
        self.___setstate__(state)
        self._compile()

    # Add new "builtins" which the script can access
    __exec = PythonScript._exec
    def _exec(self, bound_names, args, kw):
      if bound_names is None:
        bound_names = {}
      bound_names.update({f.__name__: f for f in tracing_functions})
      return self.__exec(bound_names, args, kw)

  # Apply "trace" fixers on the fly, on TALES PythonExpr
  class __(PatchClass(PythonExpr)):
    def __init__(self, name, expr, engine):
        self.text = self.expr = text = expr.strip().replace('\n', ' ')

        # Unicode expression are not handled properly by RestrictedPython
        # We convert the expression to UTF-8 (ajung)
        if isinstance(text, unicode):
            text = text.encode('utf-8')
        # <patch>
        # Patch to apply the fixers
        # XXX: "'PythonExpr:' + text" is used as the name for now. Let's try to
        # find something better.
        code, err, warn, use = compile_restricted_eval(
            apply_fixers(text, 'PythonExpr:' + text),
            self.__class__.__name__)
        # </patch>
        if err:
            raise engine.getCompilerError()('Python expression error:\n%s' %
                                             '\n'.join(err))
        self._varnames = use.keys()
        self._code = code

  # Add new "builtins" which the script can access
  PythonExpr._globals.update({f.__name__: f for f in tracing_functions})
