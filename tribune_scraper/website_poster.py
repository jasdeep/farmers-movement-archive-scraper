"""
Client ID	76331
Client Secret	jXXqWdxDdSFoDa0bU4RMapyPqKOXZIJDBz6hqJkUKHXZY7kGbBF7NTBtZFWf2TKAReset Key
Redirect URLs	https://trolleytimes.com/login/callback
Javascript Origins	https://trolleytimes.com
Type	Web
Request token URL	https://public-api.wordpress.com/oauth2/token
Authorize URL	https://public-api.wordpress.com/oauth2/authorize
Authenticate URL	https://public-api.wordpress.com/oauth2/authenticate
"""

"""
$curl = curl_init( 'https://public-api.wordpress.com/oauth2/token' );
curl_setopt( $curl, CURLOPT_POST, true );
curl_setopt( $curl, CURLOPT_POSTFIELDS, array(
    'client_id' => your_client_id,
    'redirect_uri' => your_redirect_url,
    'client_secret' => your_client_secret_key,
    'code' => $_GET['code'], // The code from the previous request
    'grant_type' => 'authorization_code'
) );
curl_setopt( $curl, CURLOPT_RETURNTRANSFER, 1);
$auth = curl_exec( $curl );
$secret = json_decode($auth);
$access_key = $secret->access_token;        
"""

website = "https://trolleytimes.com"

json_url = website + "/wp-json/wp/v2/posts"
xmlrpc_url=website+"/xmlrpc.php"
user = "jsbhangra@gmail.com"
password = "j0gewala~"

wp = Client(xmlrpc_url, user, password)

print( wp.call(GetUserInfo()))