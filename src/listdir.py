from flask import Blueprint, current_app, request

import os

listdir = Blueprint('listdir', __name__)

@listdir.route('/listdir', methods=['GET', 'POST'])
def listdir_main():
    dir = request.args.get('dir', "No directory provided")
    
    if dir == "No directory provided": 
        print(f"No directory provided")
        list_dir = list_directory("/")
    else:
        print(f"Directory: {dir}")
        list_dir = list_directory(dir)
        
    return f"->{list_dir}"


    


def list_directory(dir):
    # Establish the connection
    try:
        print("listing directory")
        os.chdir(dir)
        return os.listdir()
    except Exception as e:
        return f'Error: Unable to list directory: {e}'
