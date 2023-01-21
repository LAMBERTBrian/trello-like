import React from "react";

// hook that gets the auth state from "http://localhost:3001/auth/validate"
// and returns the user object if the user is authenticated

export const useAuth = () => {
	const [user, setUser] = React.useState<{
		user_id: number;
		user_name: string;
		user_email: string;
		user_color: string;
	} | null>(null);

	const fetchUser = async () => {
		const session_token = localStorage.getItem("session_token");

		if (!session_token) {
			return null;
		}

		const res = await (
			await fetch("http://localhost:5000/auth/validate", {
				method: "POST",
				headers: {
					"Content-Type": "application/json",
				},
				body: JSON.stringify({
					session_token,
				}),
			})
		).json();

		if (res.data.user) {
			setUser(res.data.user);
		}
	};

	React.useEffect(() => {
		fetchUser();
	}, []);

	return [user];
};
