from flask import Flask, request

app = Flask(__name__)

@app.route('/oauth2/callback')
def oauth2_callback():
    code = request.args.get('code')
    if code:
        return f"""
        <h1>Amazon OAuth2 Code</h1>
        <pre style='font-size:1.4em;color:blue'>{code}</pre>
        <p>Copy this code and use it to get your refresh token!</p>
        """
    else:
        return "<h1>No code parameter found in URL.</h1>", 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
