# Homework

Please try to develop your own, small REST API to be hosted in the cloud.

To get started,
have a look at the scenario:

## Scenario

Your customer, Northwind Traders, would like you to develop a small REST API
to support them with their inventory. Currently, employees are keeping
lists on paper, and they would like to move to a better model.

They would like the application to:
- Have a way of listing the entire inventory
- Adding new items to the inventory
  - BONUS POINTS for good error handling :)
- Removing items from the inventory
  - BONUS POINTS for good error handling :)
- Every item in inventory has the same properties
  - uid: A unique identifying number
  - name: The name of the product
  - stock: The amount if this particular item in the inventory
- BONUS POINTS FOR: Have a way of searching the inventory for certain product names

## Hints

Since we do not expect you to have access to a database, please
just declare a list or any other suitable data type to keep your inventory.
It does not matter if the list gets deleted when the app restarts.

You can either create your own class for an inventory item or you
can simply use a dictionary.

To search for product names, you might want to review how query strings
could be used.