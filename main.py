import streamlit as st
import streamlit.components.v1 as components

# bootstrap 4 collapse example
components.html(
    """
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    
   <!DOCTYPE html>
<html>

<head>
  <link rel="stylesheet" type="text/css" href="/static/styles/styles.css">
</head>

<body>
  <div class="dropdown">
    <button class="dropbtn">Dropdown</button>
    <div class="dropdown-content">
      <a href="#">Link 1</a>
      <a href="#">Link 2</a>
      <a href="#">Link 3</a>
    </div>
  </div>
  <ul>

    <li>
      <a class="navbar-brand" href="/">
        <div class="logo-image">
          <img src="/static/images/logo.png" class="img-fluid">
        </div>
      </a>
    </li>
    <li>
      <a href="#" onclick="setURL('http://localhost:8501/?p=analysis')">Analysis</a>
    </li>
    <li>
      <a href="#" onclick="setURL('http://localhost:8501/?p=results')">Results</a>
    </li>
    <li>
      <a href="#" onclick="setURL('http://localhost:8501/?p=examples')">Examples</a>
    </li>


  </ul>
  <iframe src="http://localhost:8501/?p=home" id="streamlit_content" allowfullscreen frameborder="0"
    wmode="transparent">
    Your browser doesn't support iframes
  </iframe>

</body>
<script>
  function setURL(url) {
    document.getElementById('streamlit_content').src = url;
    console.log('Works!')
  }
</script>

</html>
     
        
    """,
    height=600,
)
