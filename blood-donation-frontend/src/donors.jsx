import axios from "axios";

export const fetchDonors = async () => {
	const token = localStorage.getItem("token");

	const res = await axios.get(
		"https://<YOUR-RENDER-URL>/donors",
		{
			headers: {
				Authorization: `Bearer ${token}`,
			},
		}
	);

	return res.data;
};

export default fetchDonors;
