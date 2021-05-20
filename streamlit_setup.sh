mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"erica.yuen1996@gmail.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless=true\n\
port = $PORT\n\
" > ~/.streamlit/config.toml