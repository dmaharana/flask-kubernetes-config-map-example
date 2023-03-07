from flask import Flask, request, jsonify, redirect, render_template
import os
import logging
import configparser

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

def get_env_variable(name):
    try:
        return os.environ[name]
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        # raise Exception(message)
        return message

@app.route('/vars', methods=['GET'])
def get_env_vars():
    #  Note: /app is work dir in the container image
    #    /app/conf is created due to volume configured in deployment yaml
    config_file_path = "/app/conf/app-env.properties"
    # config_file_path = "./config-map-file/app-env.properties"

    # read from literal environment variable
    ENV_LITERAL_MYVAR = get_env_variable('ENV_LITERAL_MYVAR')
    
    # read from secret environment variable
    ENV_SECRET_MYVAR = get_env_variable('SECRET_USERNAME')
    ENV_SECRET_MYVAR2 = get_env_variable('SECRET_PASSWORD')

    logging.info(f'ENV_LITERAL_MYVAR={ENV_LITERAL_MYVAR}')
    logging.info(f'ENV_SECRET_MYVAR={ENV_SECRET_MYVAR}')

    # read config file from volume
    with open(config_file_path) as fh:
        s = fh.read()
        logging.info(f'FILE_CONTENT={config_file_path}={s}')

    # Parse config file
    config = configparser.ConfigParser()
    config.read(config_file_path)
    ENV_FILE_MYVAR = config.get("APP_ENV_VALS", "ENV_FILE_MYVAR")
    ENV_FILE_MYVAR2 = config.get("APP_ENV_VALS", "ENV_FILE_MYVAR.two")
    logging.info(f'ENV_FILE_MYVAR={ENV_FILE_MYVAR}')
    logging.info(f'ENV_FILE_MYVAR2={ENV_FILE_MYVAR2}')


    response = {
        'ENV_LITERAL_MYVAR': ENV_LITERAL_MYVAR,
        'ENV_FILE_MYVAR': ENV_FILE_MYVAR,
        'ENV_SECRET_USER': ENV_SECRET_MYVAR,
        'ENV_SECRET_PASS': ENV_SECRET_MYVAR2,
    }

    # return json.dumps(response)
    return jsonify(response)


if __name__ == '__main__':
    app.run()