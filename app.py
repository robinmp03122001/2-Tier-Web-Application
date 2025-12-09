from flask import Flask
import os
import psycopg2

app = Flask(__name__)


def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ['DB_HOST'],
        database=os.environ['DB_NAME'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASS']
    )
    return conn


@app.route('/')
def index():
    try:
        conn = get_db_connection()
        conn.close()
        return """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>2-Tier Web Application</title>
            <style>
                * {
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                }
                body {
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    min-height: 100vh;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    padding: 20px;
                }
                .container {
                    background: white;
                    border-radius: 20px;
                    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
                    padding: 50px;
                    max-width: 600px;
                    text-align: center;
                    animation: fadeIn 0.5s ease-in;
                }
                @keyframes fadeIn {
                    from {
                        opacity: 0;
                        transform: translateY(-20px);
                    }
                    to {
                        opacity: 1;
                        transform: translateY(0);
                    }
                }
                .success-icon {
                    width: 80px;
                    height: 80px;
                    margin: 0 auto 30px;
                    background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
                    border-radius: 50%;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    animation: scaleIn 0.5s ease-in-out 0.2s both;
                }
                @keyframes scaleIn {
                    from {
                        transform: scale(0);
                    }
                    to {
                        transform: scale(1);
                    }
                }
                .success-icon::before {
                    content: "✓";
                    color: white;
                    font-size: 48px;
                    font-weight: bold;
                }
                h1 {
                    color: #333;
                    font-size: 32px;
                    margin-bottom: 20px;
                    font-weight: 600;
                }
                .status {
                    color: #11998e;
                    font-size: 18px;
                    margin-bottom: 15px;
                    font-weight: 500;
                }
                .message {
                    color: #666;
                    font-size: 16px;
                    line-height: 1.6;
                    margin-bottom: 30px;
                }
                .badge {
                    display: inline-block;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                    padding: 10px 25px;
                    border-radius: 25px;
                    font-size: 14px;
                    font-weight: 600;
                    letter-spacing: 1px;
                    text-transform: uppercase;
                    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
                }
                .details {
                    margin-top: 30px;
                    padding-top: 30px;
                    border-top: 2px solid #f0f0f0;
                }
                .detail-item {
                    display: flex;
                    justify-content: space-between;
                    padding: 12px 0;
                    color: #555;
                    font-size: 14px;
                }
                .detail-label {
                    font-weight: 600;
                    color: #333;
                }
                .detail-value {
                    color: #11998e;
                    font-weight: 500;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="success-icon"></div>
                <h1>2-Tier Web Application</h1>
                <div class="status">✨ System Status: Operational</div>
                <div class="message">
                    Your 2-tier application is running successfully!<br>
                    Database connection has been established and verified.
                </div>
                <span class="badge">Connection Successful</span>
                <div class="details">
                    <div class="detail-item">
                        <span class="detail-label">Application Layer</span>
                        <span class="detail-value">✓ Active</span>
                    </div>
                    <div class="detail-item">
                        <span class="detail-label">Database Layer</span>
                        <span class="detail-value">✓ Connected</span>
                    </div>
                    <div class="detail-item">
                        <span class="detail-label">Status</span>
                        <span class="detail-value">✓ Healthy</span>
                    </div>
                </div>
            </div>
        </body>
        </html>
        """
    except Exception as e:
        return f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>2-Tier Web Application - Error</title>
            <style>
                * {{
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                }}
                body {{
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
                    min-height: 100vh;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    padding: 20px;
                }}
                .container {{
                    background: white;
                    border-radius: 20px;
                    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
                    padding: 50px;
                    max-width: 600px;
                    text-align: center;
                    animation: fadeIn 0.5s ease-in;
                }}
                @keyframes fadeIn {{
                    from {{
                        opacity: 0;
                        transform: translateY(-20px);
                    }}
                    to {{
                        opacity: 1;
                        transform: translateY(0);
                    }}
                }}
                .error-icon {{
                    width: 80px;
                    height: 80px;
                    margin: 0 auto 30px;
                    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
                    border-radius: 50%;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                }}
                .error-icon::before {{
                    content: "✕";
                    color: white;
                    font-size: 48px;
                    font-weight: bold;
                }}
                h1 {{
                    color: #333;
                    font-size: 32px;
                    margin-bottom: 20px;
                    font-weight: 600;
                }}
                .status {{
                    color: #f5576c;
                    font-size: 18px;
                    margin-bottom: 15px;
                    font-weight: 500;
                }}
                .message {{
                    color: #666;
                    font-size: 16px;
                    line-height: 1.6;
                    margin-bottom: 30px;
                }}
                .error-details {{
                    background: #fff5f5;
                    border-left: 4px solid #f5576c;
                    padding: 20px;
                    margin-top: 20px;
                    text-align: left;
                    border-radius: 8px;
                }}
                .error-details h3 {{
                    color: #f5576c;
                    font-size: 14px;
                    margin-bottom: 10px;
                    text-transform: uppercase;
                    letter-spacing: 1px;
                }}
                .error-details pre {{
                    color: #555;
                    font-size: 13px;
                    white-space: pre-wrap;
                    word-wrap: break-word;
                    font-family: 'Courier New', monospace;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="error-icon"></div>
                <h1>2-Tier Web Application</h1>
                <div class="status">⚠️ Database Connection Failed</div>
                <div class="message">
                    The application is running, but could not connect to the database.<br>
                    Please check your database configuration and try again.
                </div>
                <div class="error-details">
                    <h3>Error Details</h3>
                    <pre>{str(e)}</pre>
                </div>
            </div>
        </body>
        </html>
        """


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)