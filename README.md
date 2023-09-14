# ShelterSearch
This is a Django-based web application for a real estate website with a blog section. The project aims to provide users with a platform to browse real estate listings and read blog articles related to the real estate industry. The application is built using Django, a high-level Python web framework.

# Features
<ul>
  <li>User Registration and Authentication: Users can register and log in.</li>
  <li>Real Estate Listings: Users can browse available real estate listings, including property details, images, and contact information for the agent.</li>
  <li>Property Search: Users can search for properties based on various criteria such as location, price range, property type, and more.</li>
  <li>Blog Section: The application includes a blog section where users can read articles related to the real estate industry. Admins have the ability to create, edit, and delete blog articles.</li>
  <li>User Comments: Users can leave comments on blog articles to engage in discussions with other users.</li>
  <li>Contact Form: Users can fill out a contact form to get in touch with the website administrators.</li>
  <li>Admin Dashboard: An admin dashboard is provided for managing real estate listings, blog articles, user accounts, and other administrative tasks.</li>
</ul>

# Installation
1. Clone the repository:
   ```
   git clone https://github.com/Brainboxx/ShelterSearch.git
   ```
3. Change to the project directory:
   ```
   cd ShelterSearch
   ```
5. Create a virtual environment:
   ```
   python3 -m venv myenv
   ```
7. Activate the virtual environment:
   ```
   myenv/bin/activate
   ```
9. Install the project dependencies:
    ```
    pip install -r requirements.txt
    ```
11. Set up the database:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
13. Create a superuser (admin) account:
    ```
    python manage.py createsuperuser
    ```
15. Run the development server:
    ```
    python manage.py runserver
    ```
17. Access the application in your web browser at http://localhost:8000.

# Configuration
The application can be configured using the settings.py file located in the project's root directory. Some of the configuration options include:
<ul>
  <li>Database settings: Modify the 'DATABASES' configuration to use your preferred database (e.g., PostgreSQL, MySQL, SQLite).</li>
  <li>Email settings: Update the 'EMAIL_BACKEND' and related email configuration options to enable email functionality. </li>
  <li>Static and media files: Adjust the STATIC_URL, STATIC_ROOT, MEDIA_URL, and MEDIA_ROOT settings as per your needs.</li>
 </ul>
 
 # Usage
 <ul>
  <li>To create real estate listings, log in to the admin dashboard using the superuser account created during the installation process. Navigate to the "properties" section and click on "Add Property" to add a new property.</li>
  <li> To create blog articles, go to the admin dashboard, navigate to the "Blog" section, and click on "Add Blog Posts" </li>
  <li> Users can browse real estate listings, search for properties, read blog articles, leave comments, and contact the administrators through the website's user interface.</li>
 </ul>
 
 # Contributing
 1. Fork the repository.
 2. Create a new branch.
 3. Make your changes and commit them.
 4. Push your changes to your forked repository.
 5. Submit a pull request explaining your changes.
 
# License
This project is licensed under the MIT License.

# Credits
This application was developed by Chinedu Udochukwu Aja.







