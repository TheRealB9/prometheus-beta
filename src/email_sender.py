import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

def send_email(
    to_email: str, 
    subject: str, 
    body: str, 
    from_email: str = None, 
    smtp_server: str = None, 
    smtp_port: int = 587,
    use_tls: bool = True
) -> bool:
    """
    Send an email using SMTP with optional TLS support.
    
    Args:
        to_email (str): Recipient email address
        subject (str): Email subject
        body (str): Email body text
        from_email (str, optional): Sender email address. Defaults to environment variable.
        smtp_server (str, optional): SMTP server address. Defaults to environment variable.
        smtp_port (int, optional): SMTP server port. Defaults to 587.
        use_tls (bool, optional): Whether to use TLS. Defaults to True.
    
    Returns:
        bool: True if email sent successfully, False otherwise
    
    Raises:
        ValueError: If required email configuration is missing
    """
    # Use environment variables as fallback
    from_email = from_email or os.getenv('EMAIL_FROM')
    smtp_server = smtp_server or os.getenv('SMTP_SERVER')
    smtp_username = os.getenv('SMTP_USERNAME')
    smtp_password = os.getenv('SMTP_PASSWORD')

    # Validate required parameters
    if not all([from_email, smtp_server, smtp_username, smtp_password, to_email]):
        raise ValueError("Missing required email configuration parameters")

    try:
        # Create message container
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach body
        msg.attach(MIMEText(body, 'plain'))

        # Establish SMTP connection
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            if use_tls:
                server.starttls()
            
            # Login to SMTP server
            server.login(smtp_username, smtp_password)
            
            # Send email
            server.send_message(msg)
        
        return True

    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        return False