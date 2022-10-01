# Lowkey Menswear

This is a full-stack e-commerce project built using Django, Python, HTML, CSS and JavaScript.

Lowkey Menswear is a London based online apparel store which specialize in quality, hard-wearing clothing for an affordable price. 

The live link can be found here - [Lowkey Menswear](https://lowkey-menswear.herokuapp.com/)

![responsive](/static/images/)

# User Experience (UX)

Lowkey Menswear is a website for people aged between 18-35 to buy good quality essentials, basic's and statements pieces.

The target audience for 'Lowkey' are:
- 18 to 35 year olds
- People looking to avoid 'fast fashion'
- People looking for quality clothing

# User Stories 

#### EPIC | Navigation
- As a User I can navigate around the site so that I can easily view desired content.
- As a User, I can view a list of products so that I can choose what products to purchase.
- As a User, I can click on a product to see its details so that I can view the description, price etc.
- As a user, I can easily identify different product categories so that I can quickly view the type of products I'm looking for.
- As a User I can search for products so that I can find specific products.
- As a User, I can sort the products so that I can easily find products based on price, category, or title.
- As a User I can add items to my Wishlist so that I can save them for later.

#### EPIC | Accounts
- As a User, I can register for an account so that I can use the features given to members.
- As a User, I can receive a confirmation email when creating an account so that I know the registration was successful.
- As a User I can log in and out of my account so that I can control and manage my account
- As a User, I can recover my password in case I forget it so that I can regain access to my account.
- As a User, I can view my previous orders so that I can keep a record of what purchases I've made.
- As a User, I can save my delivery information so that I do not have to refill it out for future orders.

#### EPIC | Admin
- As an Admin, I can add products so that I can update the site's inventory.
- As an Admin, I can edit a product so that I can keep the products information up to date.
- As an Admin, I can delete a product so that I can remove products no longer available.
- As an admin, I can add coupon codes so that I can offer discounts to my customers.

#### EPIC | Purchasing
- As a User, I can add items to my basket in varying quantities so that I can keep the items in my basket until I'm ready to buy.
- As a User, I can view my bag so that I can see the total cost of the transaction and the items I will be purchasing.
- As a User, I can always see a running subtotal so that I know how much I'm spending.
- As a User, I can easily enter my payment details so that I can checkout quickly with no problems.
- As a User, I can view confirmation of my purchases so that I know the order was received and can review what I've purchased.
- As a User I can apply promotional codes so that I can receive a discount on my purchase.

#### EPIC | Interaction
- As a User I can add items to my Wishlist so that I can save them for later.
- As a User I can sign up for a newsletter to receive up to date information regarding items for sale and discounts.
- As a User, I can connect to the site's social media pages so that I can follow them and keep up to date with their products and promotions.
- As a User, I can contact the business so that I can find out any information that I require.

#### EPIC | Marketing
- As an Admin I conducted research and implemented SEO keywords to increase traffic to my website.
- As an Admin I have created a Facebook shop page to increase traffic to my website.

# Scope

In order to achieve the desired user & business goals, the following features will be included in this release:

- Responsive navbar that will navigate to the various pages throughout the site
- Landing page with image carousel with information to be found on the website
- Shop page, that displays all products available for purchase with the option to filter on the product category and price.
- My Account page, for logged in users to update their details which in turn updates the user model. User is also able to view their previous orders and wishlist.
- Register/login feature using Django AllAuth so that users can create an account.
- Custom 404 error page.

# Design

The design of the app is based on the wireframes with a mix of another clothing brand store called [COS](https://www.cos.com/en_gbp/index.html).   

## Colour Scheme
- The colour scheme for Lowkey is fairly simple, minimal and aesthetically pleasing. I used a light grey, white and some hints of black such as the black buttons to contrast the light colours of the site. I went for this style as it is clean but also because it is versatile as it matches with most colours which is important as the site would complement the colours of the product images, and keep the clothing the center of attention.

- The light grey and black are from the bootstrap light and dark classes.

## Typography
- The font used on Lowkey is Noto Sans as it is a clear and easily readable font. It is also a sleek and elegant font which goes with the theme of the site.  

## Imagery
- All the images are based on clothing and where taken from [COS](https://www.cos.com/en_gbp/index.html) and [Blacksmith-store](https://www.blacksmith-store.com/).

# Database Schema 

The design of the database can be seen below.

![Database Schema](/static/images/)

### Products

This app controls the products that are displayed in the online shop. I have created two models to store the necessary data: `Products` & `Category`.

`Products` enables individual products to be added to the database in order for them to be purchased via the online shop. Only admin users are able to access this functionality and it can be done from the front end using the `add_product` view. The admin can also edit and delete products from the front end using the `edit_product` and `delete_product` views respectively. The products model also contains the `likes` field which stores the like of a user and displays it as a wishlist item in their profile. 

This model has one Foreign Key which relates to the second model in this app, the category.

`Category` stores the various category types of the clothing on sale, this allows the user to shop by category if they are looking for something specific.

### Checkout

The checkout app is used solely for the user to make purchases via the online shop; this app contains two models, `Order` & `OrderItem`. 

`OrderItem` contains all of the information regarding the products that have been purchased as part of a specific order. It has a foreign key to `Product` & `Order`, it also contains the quantity purchased of that product and then the item total. This information is used to calculate the total cost for the order.

`Order` contains all of the relevant address information for billing/shipping, a foreign key to the `UserProfile`, email & phone number. It also contains information regarding the payment itself, the stripe PID, original basket contents (so that if the order is changed, the admin user can see what was purchased initially). Each order has an order number which is automatically generated when a new order is added to the database using `UUID`.

There are some other model methods used at various points, `update_total` calculates the overall total including any coupons that have been used depending on the order items linked to the order, ensuring the value is always correct.

### Profile

The profile app enables authenticated users to save their information so that when they are logged in the order form is pre-filled, creating an improved user experience. The `UserProfile` model is linked to the Django AllAuth user account.