import axios from "axios";

export const fetchDonors = async () => {
	const token = localStorage.getItem("token");

	const res = await axios.get(
		"https://blood-donation-system-c82d.onrender.com/donors",
		{
			headers: {
				Authorization: `Bearer ${token}`,
			},
		}
	);

	return res.data;
};

export default fetchDonors;
