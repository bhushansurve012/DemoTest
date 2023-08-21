import streamlit as st

st.title("Binance Price App")

# CSS for navbar
navbar_style = """
.navbar {
    margin-top: 30px;
}
"""

# Apply the navbar CSS
st.markdown(f'<style>{navbar_style}</style>', unsafe_allow_html=True)

# Navbar HTML code
navbar_html = """
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <a class="navbar-brand" href="#">
        <img src="https://via.placeholder.com/30" width="30" height="30" class="d-inline-block align-top" alt="">
        NTT Data
    </a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav"
        aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
            <li class="nav-item active">
                <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
            </li>
            <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button"
                    data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    Dropdown
                </a>
                <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                    <a class="dropdown-item" href="#">Action</a>
                    <a class="dropdown-item" href="#">Another action</a>
                    <div class="dropdown-divider"></div>
                    <a class="dropdown-item" href="#">Something else here</a>
                </div>
            </li>
        </ul>
    </div>
</nav>
"""

# Apply the navbar HTML
st.markdown(navbar_html, unsafe_allow_html=True)

st.header("Binance Price App")
st.write("A simple cryptocurrency price app pulling price data from Binance API.")
