#  PDF2texto :sparkles:

Welcome to **PDF2TEXTO**:sparkles:,

This is an open source project to deploy a webpage, upload a pdf file and download their .txt file content. 

There are 2 versions available:

* [PDF2texto.v.1](https://pdf2texto.streamlit.app/): only works for selectable text (the code is this repo).
* [PDF2texto.v.2](https://github.com/Lidiasaes/PDF2texto/blob/main/Streamlit_Colaboratory/Streamlit_PDF2texto_v_2.ipynb): works for any type of pdf file (OCR implemented; the code is found in folder Streamlit_Colaboratory).


**How to use it?**
1. Run the Colaboratory notebook cell by cell.
2. The last cell will return an output similar to this one:
```
You can now view your Streamlit app in your browser.
 
Local URL: http://localhost:8501

Network URL: http://123.45.6.78:8501

External URL: http://12.345.678.90:8501
 
 
npx: installed 22 in 2.441s
 
your url is: https://nice-forks-start.loca.lt
```

3. In 'External URL', copy the number appearing between https and the port (:8501). In this example: 12.345.678.904
4. Click in 'your url is:'. It will pop up a new window.
5. Paste the number you copied in step 3. Click 'Submit'. It will start running :sparkles::sparkles::sparkles:


------------------------------
I used [this tutorial](https://www.youtube.com/watch?v=VqgUkExPvLY) as first steps for building the website with Streamlit




# Language2Language :sparkles:
This is the second part of the project. You can upload a .txt file. Select the source language, the target language, and automatically translate it! This code uses [these models](https://github.com/Helsinki-NLP/Opus-MT). 

Not all languages are supported, as this is a prototype, the ones you may find in [this list](https://developers.google.com/admin-sdk/directory/v1/languages?hl=es-419). If you want more, just add them easily! :sparkles:

You may need an account on Hugging Face in order to get your own Acess Token
