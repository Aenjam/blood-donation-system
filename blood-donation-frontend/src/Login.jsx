import axios from "axios";

function Login() {
  const handleLogin = async () => {
    try {
      const res = await axios.post(
        "https://blood-donation-system-c82d.onrender.com/login",
        {
          username: "admin",
          password: "admin"
        }
      );

      // ✅ STORE TOKEN
      localStorage.setItem("token", res.data.access_token);

      alert("Login successful");
    } catch (err) {
      console.error(err.response?.data || err.message);
      alert("Login failed");
    }
  };

  return (
    <>
      <h2>Login</h2>
      <button onClick={handleLogin}>Login</button>
    </>
  );
}

export default Login;
