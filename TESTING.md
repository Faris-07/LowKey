# Manual Testing

[Back to main README](README.md)

### EPIC | Navigation
- As a User I can navigate around the site so that I can easily view desired content.

    - The navigation bar is fixed at the top of the screen, meaning it is always seen by the user, allowing the user to navigate through the content easily & intuitively. Each nav link is named with an obvious link to the page content, for the shop and admin links there are dropdowns for subsections of the website so that there isn't too much information in the navbar.
    - I have tested that the navbar is fully responsive on all screen sizes and remains at the top of each page.
    ![](assets/images/)

    - Also located in the footer are quick links, which has links to all pages of the website.
    ![](assets/images/)

    - I have added a back to top button that appears when the user scrolls down any of the pages, enabling them to quickly navigate back to the top without having to scroll.
    - I have tested that the scroll button works and is responsive.
    ![](assets/images/)

- As a User, I can view a list of products so that I can choose what products to purchase.
    - From the navbar, users can click the 'Shop' link and in the dropdown menu choose 'All Products' to be taken to the product's page, which will list every product on the store.

    ![](assets/images/)

- As a User, I can click on a product to see its details so that I can view the description, price etc.
    - By clicking the product's image, the user is taken directly to the product's detail page, where the name, description, size, composition, quantity and price are displayed.
    ![](assets/images/)

- As a user, I can easily identify different product categories so that I can quickly view the type of products I'm looking for.
    - From the navbar, users can click the 'Shop' link and in the dropdown and choose any category they want to view which will show a product's page, that will list every product on the store under that category.
    - From the home page, users can also find the 'Essentials' section where four featured categories are listed. Clicking either of these images takes the user to the products page, showing only items in that category.
    ![](assets/images/)

- As a User I can search for products so that I can find specific products.
    - Located in the center of the navbar is a search bar. On smaller screens, the search bar is in the hamburger menu. Any searched word will match itself to any text in the product's title, or description and display the results on the product's page.
    ![](assets/images/)

- As a User, I can sort the products so that I can easily find products based on price, category, or title.
    - A sort selector box is located on the products page where users can sort all products by price.
    ![](assets/images/)

- As a User I can add items to my Wishlist so that I can save them for later.
    - Liked products will appear in the user's wishlist items list, located on the user's profile page.
    ![](assets/images/)

### EPIC | Accounts
- As a User, I can register for an account so that I can use the features given to members.
    - Users can click the 'Sign in/up' accounts icon located in the header of the page, and from there click the link 'Register'.
Once on the registration page, users can fill in a short form to sign up for a Lowkey account.
    ![](assets/images/)

- As a User, I can receive a confirmation email when creating an account so that I know the registration was successful.
    - Once the registration form has been submitted, the user will be sent a confirmation email which contains a link that the user has to follow to confirm their account.
    ![](assets/images/)

- As a User I can log in and out of my account so that I can control and manage my account
    - Once a user has created an account they can log-in using the profile icon in the navbar.
    ![](assets/images/)

- As a User, I can recover my password in case I forget it so that I can regain access to my account.
    - If a user forgets their password they can click the link in the login page to recieve an email so that they can create a new password.
    ![](assets/images/)

- As a User, I can view my previous orders so that I can keep a record of what purchases I've made.
    - Once a user has created an account and placed an order, they can view their order's in their profile section located under the accounts menu.
Clicking the user's order number will take you to a summary page of that order.
    ![](assets/images/)

- As a User, I can save my delivery information so that I do not have to refill it out for future orders.
    - Users can fill in their delivery information on their profile page. This information will autofill the checkout form when the user checkouts.
    - When placing an order a checkbox under the delivery information can be checked to save the information added to the form.
    ![](assets/images/)

### EPIC | Admin
- As an Admin, I can add products so that I can update the site's inventory.
    - Admins can navigate to the 'Manage' page under the accounts menu.
    - Once on the product management page the admin can add new products by filling out the 'add product form'.
    ![](assets/images/)

- As an Admin, I can edit a product so that I can keep the products information up to date.
    - If an admin is logged in, the edit button will be displayed in the product detail page.
    - When the 'Edit' button is clicked the admin is taken to the 'Edit product' page. The admin can then edit existing products using the 'edit product form'.
    ![](assets/images/)

- As an Admin, I can delete a product so that I can remove products no longer available.
    - If an admin is logged in, the delete button will be displayed in the product detail page.
    - When the 'delete' button is clicked a confirmation model is diplayed asking the admin if they want to delete the specific product.
    - If the admin wants to delete the product they click delete, else if they no longer want to delete the product they can press the 'cancel' button or click outside of the modal to exit the confirmation modal.
    ![](assets/images/)

- As an admin, I can add coupon codes so that I can offer discounts to my customers.
    - Admins can navigate to the 'Coupon' page under the accounts menu.
    - Once on the coupon management page the admin can add new coupons by filling out the 'add coupon form'.
    ![](assets/images/)

#### EPIC | Purchasing
- As a User, I can add items to my basket in varying quantities so that I can keep the items in my basket until I'm ready to buy.
    - On the product's detail page, shoppers can adjust the quantity by using the quantity selector, or by typing in the amount and clicking the 'Add to bag' button, to add the item to the bag.
    - At the bottom of the products card, is an 'Add to Bag' button which adds 1 item to the bag by default.
    ![](assets/images/)

- As a User, I can view my bag so that I can see the total cost of the transaction and the items I will be purchasing.
    - Clicking the bag icon in the top right corner will take the user to their bag.
    - The shopping bag page lists the items added by the user, along with the subtotal of each item, delivery costs, and the total to pay.
    ![](assets/images/)

- As a User, I can always see a running subtotal so that I know how much I'm spending.
    - The bag icon will update automatically to reflect how many items are in the bag.
    - The user will also get success toast messages for every product they add to their bag which displays the bag items, quantity, size and bag total.
    ![](assets/images/)

- As a User, I can easily enter my payment details so that I can checkout quickly with no problems.
    - Paying for items is simple as the user enters their card details into the payment box on the checkout page and click the 'Complete Order' button.
    ![](assets/images/)

- As a User, I can view confirmation of my purchases so that I know the order was received and can review what I've purchased.
    - After an order has been completed, the user will be taken to a confirmation page with a summary of the order.
    - Users will also recieve a confirmation email of their order.
    ![](assets/images/)

- As a User I can apply promotional codes so that I can receive a discount on my purchase.
    - Users can use coupon codes to take off a certain percent of their order.
     ![](assets/images/)