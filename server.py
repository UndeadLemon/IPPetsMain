from ip_pets import app
from ip_pets.controllers import users, pets


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.