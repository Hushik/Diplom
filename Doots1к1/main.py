from flask import Flask
from website import create_app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host="100.98.14.139", port=5000)