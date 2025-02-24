import os
import pytest
from src.email_sender import send_email

# Mock environment variables for testing
os.environ['EMAIL_FROM'] = 'test@example.com'
os.environ['SMTP_SERVER'] = 'smtp.example.com'
os.environ['SMTP_USERNAME'] = 'testuser'
os.environ['SMTP_PASSWORD'] = 'testpassword'

def test_send_email_missing_params():
    """Test that function raises ValueError when parameters are missing"""
    # Temporarily unset environment variables
    original_env = {key: os.getenv(key) for key in ['EMAIL_FROM', 'SMTP_SERVER', 'SMTP_USERNAME', 'SMTP_PASSWORD']}
    try:
        os.unsetenv('EMAIL_FROM')
        os.unsetenv('SMTP_SERVER')
        os.unsetenv('SMTP_USERNAME')
        os.unsetenv('SMTP_PASSWORD')

        with pytest.raises(ValueError, match="Missing required email configuration parameters"):
            send_email(to_email=None, subject="Test", body="Test body")
    finally:
        # Restore environment variables
        for key, value in original_env.items():
            os.environ[key] = value or ''

def test_send_email_parameters():
    """Test that function accepts correct parameters"""
    result = send_email(
        to_email='recipient@example.com', 
        subject='Test Subject', 
        body='Test Body'
    )
    # In a real test, this would be mocked
    assert result is False

def test_invalid_server_details():
    """Test handling of invalid SMTP server details"""
    result = send_email(
        to_email='recipient@example.com', 
        subject='Test Subject', 
        body='Test Body',
        smtp_server='invalid.server',
        smtp_port=25
    )
    # Should return False due to connection failure
    assert result is False

def test_email_structure():
    """Validate email structure parameters"""
    with pytest.raises(TypeError):
        # Intentionally pass incorrect types to test type checking
        send_email(to_email=123, subject=None, body=object())  # type: ignore

def test_empty_parameters():
    """Test empty parameter handling"""
    with pytest.raises(ValueError):
        send_email(to_email='', subject='', body='Test Body')

def test_non_string_parameters():
    """Test non-string parameter handling"""
    with pytest.raises(TypeError):
        send_email(to_email=123, subject=456, body=object())