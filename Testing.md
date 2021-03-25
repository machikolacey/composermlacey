# Testing

### User stories
### Visitor
| User Story    | Expected Outcome  | Actual Outcome | 
|:------------- |:---------------|:--------------------|
| I would like to find out up-coming events and recent albums on top of the homepage | so I can find out up-coming events and recent albums at a glance   | I could find homepage banner easily to find out up-coming events |
| I would like to navigate to the destination page smoothly | so I can find the information I want easily  |   The navigation is easy to use, and nav links are well-structured to find information I want               |
| I would like to find schedule easily | so I can find event dates in no time   |  result|
| I would like to find out what is the artist's motivation on her composition | so I can see if her music suits my interest     |  Under 'about' dropdown there are links to information pages, and easy to find out about the composition |
| I would like to find out about genre of the artist's songs  | so I can see if her music suits my interest |  'Neo Classical Piano' page gives a good information to know the genre |
| I would like to listen to samples of her songs	  | so I can see if the music feeds my interest |  On 'Sample videos' page I could listen to samples easily.  |
| I would like to see how album jackets look like	  | so I can find it the album interests me |  I could see album jacket on the shop/ category/ product page |
| I would like to find out venue, date, time and duration of the event  | so I can find out if I can attend it. |  I could find event details on event product page |
| I would like to purchase the artist's products and event tickets  | so I can enjoy her music. |  I could purchase the CD album through product, cart and checkout |
| I would like to write a review on my purchased products  | so I can share my thoughts on my purchased products.   |  I could find review section on product page and add a review when logged in |
| 	I would like to be able to purchase the products securely  | so I feel safe through payment section.|  I could feel safe on payment page, using Stripe |
| I would like to be able to register on this website  | so I can purchase easily in the future. |  I could register an account at ease |
| I would like to be able to reset my password	  | so I can login again in case I forget my password|  I could reset my password at ease |
| I would like to be able to see my order history	  | so I can see what I purchased |  I could see my order history on profile page when logged in |
| I would like to be able to update the account details	  | so I can update my address, phone number etc in case I change them   |  I could update my details on 'Profile' page |



### Site Owner
| User Story    | Expected Outcome  | Actual Outcome | 
|:------------- |:---------------|:--------------------|
| I would like to be able to add a product easily | so I feel ease on adding product | I could add a product at ease |
| I would like to be able to edit a product easily	 | so I can update product details at ease | I could edit a product at ease |
| I would like to be able to delete a product	 | so it won't show up on the website. | I could delete a product at ease |
| I would like to be able to add album songs | so they will be displayed on the album product page | I could add album songs at ease |
| I would like to be able to add event venue, date, time and duration | so they will be displayed on the event product page | I could add event venue, date, time, and duration at ease |
| I would like to be able to modify event details	 | so I can update event details | I could modify event details at ease |
| I would like to be able to update artist information pages | so I can flexibly refresh the page information | I could update information pages at ease |


## Issues found
| Issue    | How I fixed it  |
|:------------- |:---------------|
|The stylings was not attached to sign up page | added block inner_content onto the template |
|The navbar was too large between 1020px and 768px| added more media queries to keep the same height |
|On review section there was nothing mentioned when the user was logged out | Added a text to navigate users|
|Navbar dropdown was too narrow on tablet size | Added css to make sure the dropdown is 100%|
|Event start date, time was not displayed | Added the code on the template with Jinja formatter|
|The header was full width, rather than container width | added container under header tag|

## Issues mentioned by code reviews

| Issue    | How I fixed it  |
|:------------- |:---------------|
|Possibly need extra time delay switching between the 2 hero images | result |
|Need different images for different albums/ events|result|
|Title needs to be consistent - '2021 summer concert' to be '2021 Summer Concert'|result|
|each of the sub menu options under ABOUT I get a blank screen with "Page Template" on the way to displaying the required page|result|
|The link to the bag is not visible on mobilephone|result|
|The navigator is overflowing on Slick slider|result|
|When signed up, confirmation email was not received|result|
|On mobile phone, the toast message is pointing nowhere|result|



## Validators
This was ran through these validators.

<ul>
<li><a href="https://validator.w3.org/" target="_blank">W3C HTML Validations</a></li>
<li><a href="https://jigsaw.w3.org/css-validator/" target="_blank">W3C CSS Validations</a></li>
<li><a href="http://pep8online.com/" target="_blank">PEP8 Online Checker</a></li>
<li><a href="http://jshint.com/" target="_blank">JSHint, A Static Code Analysis Tool for JavaScript</a></li>
</ul>

### Result - W3C HTML Validations

| Issue    | How I fixed it  |
|:------------- |:---------------|
|Error: Element li not allowed as child of element nav in this context. (Suppressing further errors from this subtree.) | Added ul above the li tags|
|Error: No p element in scope but a p end tag seen.| Replaced p tag with div tag on one of them |
|The frameborder attribute on the iframe element is obsolete. Use CSS instead.| Removed frameborder=0 on iframe tags |

### Result - W3C CSS Validations
| Issue    | How I fixed it  |
|:------------- |:---------------|
|Value Error : font-size only 0 can be a unit. You must put a unit after your number : 16| added '1 rem' instead of '16'|


Other errors are coming from Font Awesome, Bootstrap which is recommended by Code Institute. We have no controll over them.

<img src="https://res.cloudinary.com/machikolacey/image/upload/v1616623997/milestone4/w3ccss_xirbio.png" />