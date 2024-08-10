# Project Title: 
### **Creating a Session Fixation Issue with Predictable Session ID Generation.**

## Project Description

In this project, we aim to demonstrate a security vulnerability known as session fixation through the generation of predictable session IDs. Session fixation is a type of attack where the attacker tricks a user into authenticating with a session ID known to the attacker, allowing the attacker to hijack the session once the user has authenticated.

## Objective

The primary objective of this project is to showcase how a web application with a predictable session ID generation mechanism is vulnerable to session fixation attacks. We will develop a web application that intentionally generates session IDs in a predictable manner and demonstrate how an attacker can exploit this weakness.

## Key Features

### Web Application with Login Functionality
- A simple web application with a login system.
- Users can log in with a username and password.

### Predictable Session ID Generation
- The application will generate session IDs in a predictable sequence (e.g., 12345, 1234510, etc.).
- Session IDs will be hardcoded or follow a simple, predictable pattern.

### Session Fixation Vulnerability
- The application will not regenerate the session ID upon user authentication.
- An attacker can set a session ID before the user logs in and then use the same session ID to gain unauthorized access after the user authenticates.

## Implementation Details

### Programming Language
- Python (Flask for web application)
### Tools
- Web browser for testing
- Development environment (PyCharm)
- Burp Suite for intercepting and manipulating HTTP requests
### Libraries
- Flask for web framework
## Expected Outcome

By the end of this project, we will have a working web application that clearly demonstrates the session fixation vulnerability due to predictable session ID generation. The project will highlight the importance of secure session management practices and provide insights into how to prevent such vulnerabilities in real-world applications.

## Conclusion

This project serves as an educational tool for understanding session fixation attacks and the risks associated with predictable session IDs. It underscores the importance of implementing robust security measures in web applications to safeguard against such vulnerabilities.
