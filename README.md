#PoRedit

Simple online PO/POT translation file editor. Built on Flask and Python PoLib.

####What it does?
Just a simple thing, I could upload a .po or .pot file to this app, I got the edit link, and send the link to my partner that will do the translation.

My partner do translation online through web based interface, when he cannot finish it today, he just need to save it and open the link again tomorrow. When he's finished, he just need to tell me and I am ready to download it as its .po format or download the compiled version (.mo) file.

That's it, I think it's better way than sending the .po file back and forth via email when it need some changes.

####How it built?
This app built entirely on top of Open Source software such as:

- **Flask**, a micro web framework built on Python. It's just perfect for this kind of task and utility. Although it can be used to create large a scale web apps too.
- **PoLib**, a Python module that can be used to create, read and modify PO and MO translation file.
- **Bootstrap** from Twitter, just an amazing UI framework that can let me focus on the backend code, and let Bootstrap handle the beautiful think at the front.

I don't know if there are something similar to this app out there, and even there are much better than this one. I just like to built something by rolling my own head, learn something new every day, as long as I have enough time on it, I will do it.
