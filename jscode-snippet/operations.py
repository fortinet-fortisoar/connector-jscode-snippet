from connectors.core.connector import get_logger, ConnectorError
import js2py


logger = get_logger('jscode_snippet')

def run_js_code(config, params):
    try:
        js_code = params.get('js_code')
        js_code = js_code.replace("document.write", "return ")
        js2py.eval_js(js_code)
        return {'data':js2py.eval_js(js_code), 'Status':'Success'}

    except Exception as exp:
        logger.exception('Error Executing Code: {}'.format(exp))
        raise ConnectorError('Error Executing Code: {}'.format(exp))

def _check_health(config):
    try:
        import js2py
        return True
    except:
        logger.exception('Module: js2py not found')
        raise ConnectorError('Module: js2py not found')


operations = {
    'run_js_code': run_js_code
}
