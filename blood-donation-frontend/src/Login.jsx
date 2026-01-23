import axios from "axios";

function Login() {
  const handleLogin = async () => {
    try {
      const res = await axios.post(
        "https://<YOUR-RENDER-URL>/login"
      );

      localStorage.setItem("token", res.data.access_token);
      alert("Login successful");
    } catch (err) {
      alert("Login failed");
      console.error(err);
    }
  };

  return <button onClick={handleLogin}>Login</button>;
}

export default Login;
