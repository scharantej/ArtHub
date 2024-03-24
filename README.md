## Flask Application Design

### HTML Files
- **index.html** - Main page of the website containing the list of sample images and their respective descriptions.
- **gallery.html** - Page featuring a gallery of all available sample images.
- **about.html** - Page providing details about the art gallery, its mission, and its artists.

### Routes

- **"/"** - Home route that displays the index.html page.
- **"/gallery/"** - Route for the gallery page, which displays the gallery.html page.
- **"/about/"** - Route for the about page, which displays the about.html page.
- **"/images/"** - Route for serving the image files used on the website.
- **"/image/<filename>"** - Route for retrieving an image file by its filename.