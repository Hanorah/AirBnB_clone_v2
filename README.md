# AirBnB Clone - The Console(First Part)

The console is the first component of ALX's AirBnB project, which will cover fundamental concepts of higher level programming. The goal of the AirBnB project is to eventually deploy a simple copy of the AirBnB website on our server (HBnB). In this segment, a command interpreter is created to manage objects for the AirBnB(HBnB) website.The console is the first segment of the AirBnB project at Hol School that will collectively cover fundamental concepts of higher level programming. The goal of AirBnB project is to eventually deploy our server a simple copy of the AirBnB Website(HBnB). A command interpreter is created in this segment to manage objects for the AirBnB(HBnB) website.

The first piece(The Console) is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine.

#### Features of the console:

- Create a new data model
- Retrieve an object from a file, a database etc...
- Do operations on objects (count, compute stats, etc...)
- Update attributes of an object
- Destroy an object

#### Usage

- Clone this repository: `git clone "https://github.com/shakvilla/AirBnB_clone.git"`
- Access AirBnb directory: `cd AirBnB_clone`
- Run hbnb(interactively): `./console` and enter command
- Run hbnb(non-interactively): `echo "<command>" | ./console.py`
