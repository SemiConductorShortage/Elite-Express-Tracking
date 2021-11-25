# Elite-Express-Tracking
Track Your Elite Express Packages with this CLI tool! [More of a simple Library]
## Have you ever wanted a way to track packages in Elite Express in a CLI, either for your data-collection needs or for your personal use?
Now you can, with this simple library. 

There are only two functions (It's a class and a function but okay)

- One to fetch data
- One to fetch data and print it out nicely


![image](https://user-images.githubusercontent.com/83015532/143492773-9cd237a4-0d49-4c0c-a506-8c2d253ceb7f.png)\
How it looks like when its printed nicely^


Using it is pretty straightforward, just download the source, and shove the EliteExpress folder inside your project directory

From there on, you can use the `getInfo` class like so:

```
import EliteExpress
Info = EliteExpress.getInfo(<Airwaybill Number>)
```
We'll be using the example above to demonstrate what it does.

- `Info.places` will return a List object containing the places it's been to, usually the 3 letter code for it [String].
- `Info.details` will return a dictionary containing the shipping processes that have taken place, and the timestamp of when each step happened, accessible by its dictionary keys
- `Info.FirstName` returns the First Name of the package receiver [Public data][String].
- `Info.weight` returns a string showing the weight of the package, presumably in Kilograms [The accuracy of this is dependant on Elite Express][String].
- `Info.shipmentDate` returns the shipment date, assuming it's when the shipping started rather than when it ended [String]. 
- `Info.origin` returns the origin country of the package [String].
- `Info.destination` returns the country that it the package is going to [String].
- `Info.count` shows the amount of packages that have been ordered by the user [String].

That should cover it all!

To get a `pretty table`, just run `EliteExpress.styleData(<Airwaybill Number>)` and it should print the data. If you want it in a different format, feel free to modify this!
