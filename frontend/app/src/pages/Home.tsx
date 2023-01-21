import React from "react";
import { useAuth } from "../hooks/auth";
import { Link } from "react-router-dom";
import { Button } from "../components/Button";

export const Home = () => {
	const [user] = useAuth();

	const [loading, setLoading] = React.useState<boolean>(false);

	const logout = async () => {
		const session_token = localStorage.getItem("session_token");

		if (!session_token) {
			return null;
		}

		setLoading(true);

		const res = await (
			await fetch("http://localhost:5000/auth/logout", {
				method: "POST",
				headers: {
					"Content-Type": "application/json",
				},
				body: JSON.stringify({
					session_token,
				}),
			})
		).json();

		if (res.validated) {
			localStorage.removeItem("session_token");

			window.location.reload();
		}

		setLoading(false);
	};

	return (
		<div className="w-full h-screen flex flex-col justify-center items-center gap-8">
			<h1 className="text-5xl font-bold">Tasky</h1>
			<div className="bg-secondary-bg rounded-lg flex justify-center items-center p-6">
				{user ? (
					<div className="flex flex-col gap-4 justify-center items-center">
						<p className="text-lg">You are logged in as {user.user_name}</p>
						<Button
							onClick={logout}
							loading={loading}
						>
							Log out
						</Button>
						<Link to="/dashboard">
							<Button onClick={() => {}}>Go to dashboard</Button>
						</Link>
					</div>
				) : (
					<div className="flex flex-col gap-4 justify-center items-center">
						<p className="">You are not logged in</p>

						<div className="flex gap-4">
							<Link to="/login">
								<Button onClick={() => {}}>Log in</Button>
							</Link>
							<Link to="/signup">
								<Button onClick={() => {}}>Sign Up</Button>
							</Link>
						</div>
					</div>
				)}
			</div>
		</div>
	);
};
