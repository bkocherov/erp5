web_section = context

if REQUEST is not None:
  modification_date_string = web_section.getModificationDate().rfc822()
  weak_etag_header = 'W/"%s"' % modification_date_string
  REQUEST.RESPONSE.setHeader('ETag', weak_etag_header)
  if_none_match = REQUEST.getHeader('If-None-Match', '')
  #using 'in' instead of '==' because the header value may contain a suffix
  #for the server HTTP compression. e.g. "-gzip" suffix for DeflateAlterETag on apache
  if weak_etag_header[:-1] in if_none_match:
    REQUEST.RESPONSE.setStatus(304)
    return ""

# Add all ERP5JS gadget
url_list = [
  'favicon.ico',
  'font-awesome/font-awesome-webfont.eot',
  'font-awesome/font-awesome-webfont.woff',
  'font-awesome/font-awesome-webfont.woff2',
  'font-awesome/font-awesome-webfont.ttf',
  'font-awesome/font-awesome-webfont.svg',
  'gadget_erp5_worklist_empty.svg',
  'erp5_launcher_nojqm.js',
  'gadget_erp5_nojqm.css',
  'gadget_erp5_configure_editor.html',
  'gadget_erp5_configure_editor.js',
  'gadget_erp5_editor_panel.html',
  'gadget_erp5_editor_panel.js',
  'gadget_erp5_field_checkbox.html',
  'gadget_erp5_field_checkbox.js',
  'gadget_erp5_field_datetime.html',
  'gadget_erp5_field_datetime.js',
  'gadget_erp5_field_editor.html',
  'gadget_erp5_field_editor.js',
  'gadget_erp5_field_email.html',
  'gadget_erp5_field_email.js',
  'gadget_erp5_field_file.html',
  'gadget_erp5_field_file.js',
  'gadget_erp5_field_float.html',
  'gadget_erp5_field_float.js',
  'gadget_erp5_field_formbox.html',
  'gadget_erp5_field_formbox.js',
  'gadget_erp5_field_gadget.html',
  'gadget_erp5_field_gadget.js',
  'gadget_erp5_field_image.html',
  'gadget_erp5_field_image.js',
  'gadget_erp5_field_integer.html',
  'gadget_erp5_field_integer.js',
  'gadget_erp5_field_label.html',
  'gadget_erp5_field_label.js',
  'gadget_erp5_field_list.html',
  'gadget_erp5_field_list.js',
  'gadget_erp5_field_lines.html',
  'gadget_erp5_field_lines.js',
  'gadget_erp5_field_listbox.html',
  'gadget_erp5_field_listbox.js',
  'gadget_erp5_field_matrixbox.html',
  'gadget_erp5_field_matrixbox.js',
  'gadget_erp5_field_multicheckbox.html',
  'gadget_erp5_field_multicheckbox.js',
  'gadget_erp5_field_multilist.html',
  'gadget_erp5_field_multilist.js',
  'gadget_erp5_field_parallellist.html',
  'gadget_erp5_field_parallellist.js',
  'gadget_erp5_field_multirelationstring.html',
  'gadget_erp5_field_multirelationstring.js',
  'gadget_erp5_field_radio.html',
  'gadget_erp5_field_radio.js',
  'gadget_erp5_field_readonly.html',
  'gadget_erp5_field_readonly.js',
  'gadget_erp5_field_relationstring.html',
  'gadget_erp5_field_relationstring.js',
  'gadget_erp5_field_string.html',
  'gadget_erp5_field_string.js',
  'gadget_erp5_field_password.html',
  'gadget_erp5_field_password.js',
  'gadget_erp5_field_textarea.html',
  'gadget_erp5_field_textarea.js',
  'gadget_erp5_form.html',
  'gadget_erp5_form.js',
  'gadget_erp5_header.html',
  'gadget_erp5_header.js',
  'gadget_erp5_jio.html',
  'gadget_erp5_jio.js',
  'gadget_erp5_label_field.html',
  'gadget_erp5_label_field.js',
  'gadget_erp5_notification.html',
  'gadget_erp5_notification.js',
  'gadget_erp5_page_action.html',
  'gadget_erp5_page_action.js',
  'gadget_erp5_page_export.html',
  'gadget_erp5_page_export.js',
  'gadget_erp5_page_form.html',
  'gadget_erp5_page_form.js',
  'gadget_erp5_page_front.html',
  'gadget_erp5_page_front.js',
  'gadget_erp5_page_history.html',
  'gadget_erp5_page_history.js',
  'gadget_erp5_page_jump.html',
  'gadget_erp5_page_jump.js',
  'gadget_erp5_page_language.html',
  'gadget_erp5_page_language.js',
  'gadget_erp5_page_logout.html',
  'gadget_erp5_page_logout.js',
  'gadget_erp5_page_preference.html',
  'gadget_erp5_page_preference.js',
  'gadget_erp5_page_relation_search.html',
  'gadget_erp5_page_relation_search.js',
  'gadget_erp5_page_search.html',
  'gadget_erp5_page_search.js',
  'gadget_erp5_page_tab.html',
  'gadget_erp5_page_tab.js',
  'gadget_erp5_page_worklist.html',
  'gadget_erp5_page_worklist.js',
  'gadget_erp5_panel.html',
  'gadget_erp5_panel.js',
  'gadget_erp5_panel.png',
  'gadget_erp5_pt_embedded_form_render.html',
  'gadget_erp5_pt_embedded_form_render.js',
  'gadget_erp5_pt_form_dialog.html',
  'gadget_erp5_pt_form_dialog.js',
  'gadget_erp5_pt_form_jump.html',
  'gadget_erp5_pt_form_jump.js',
  'gadget_erp5_pt_form_list.html',
  'gadget_erp5_pt_form_list.js',
  'gadget_erp5_pt_form_python_action.html',
  'gadget_erp5_pt_form_python_action.js',
  'gadget_erp5_pt_form_view.html',
  'gadget_erp5_pt_form_view.js',
  'gadget_erp5_pt_form_view_editable.html',
  'gadget_erp5_pt_form_view_editable.js',
  'gadget_erp5_pt_report_view.html',
  'gadget_erp5_pt_report_view.js',
  'gadget_erp5_router.html',
  'gadget_erp5_router.js',
  'gadget_erp5_relation_input.html',
  'gadget_erp5_relation_input.js',
  'gadget_erp5_search_editor.html',
  'gadget_erp5_search_editor.js',
  'gadget_erp5_searchfield.html',
  'gadget_erp5_searchfield.js',
  'gadget_erp5_sort_editor.html',
  'gadget_erp5_sort_editor.js',
  'gadget_global.js',
  'gadget_html5_element.html',
  'gadget_html5_element.js',
  'gadget_html5_input.html',
  'gadget_html5_input.js',
  'gadget_html5_textarea.html',
  'gadget_html5_textarea.js',
  'gadget_html5_select.html',
  'gadget_html5_select.js',
  'gadget_erp5_global.js',
  'gadget_jio.html',
  'gadget_jio.js',
  'gadget_translation.html',
  'gadget_translation.js',
  'gadget_translation_data.js',
  'gadget_editor.html',
  'gadget_editor.js',
  'gadget_button_maximize.html',
  'gadget_button_maximize.js',
  'domsugar.js',
  'jiodev.js',
  'renderjs.js',
  'rsvp.js',
]

# Add all root gadgets
default_url = './'
available_language_set = web_section.getLayoutProperty("available_language_set", default=['en'])
default_language = web_section.getLayoutProperty("default_available_language", default='en')
for language in available_language_set:
  if language == default_language:
    url_list.append(default_url)
  else:
    url_list.append('%s/' % language)

# Add all custom gadgets
url_list.extend([
  web_section.getLayoutProperty("configuration_wallpaper_url", default=default_url),
  web_section.getLayoutProperty("configuration_panel_gadget_url", default=default_url),
  web_section.getLayoutProperty("configuration_router_gadget_url", default=default_url),
  web_section.getLayoutProperty("configuration_header_gadget_url", default=default_url),
  web_section.getLayoutProperty("configuration_jio_gadget_url", default=default_url),
  web_section.getLayoutProperty("configuration_translation_gadget_url", default=default_url),
  web_section.getLayoutProperty("configuration_stylesheet_url", default=default_url),
  web_section.getLayoutProperty("configuration_icon_url", default=default_url),
])

# Add all extra dependencies
precache_manifest_url_list = web_section.getLayoutProperty("configuration_precache_manifest_script_list", default='').splitlines()
for precache_manifest_script_id in precache_manifest_url_list:
  url_list.extend(web_section.restrictedTraverse(precache_manifest_script_id)())

if REQUEST is not None:
  import json
  REQUEST.RESPONSE.setHeader('Content-Type', 'application/json')
  return json.dumps(dict.fromkeys(url_list), indent=2)

return list(set(url_list))
