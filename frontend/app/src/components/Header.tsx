import { useCallback, useEffect, useState } from "react";
import { useAuth } from "../hooks/auth";
import { Button } from "./Button";
import { Link } from "react-router-dom";

export const Header = () => {
	const [user] = useAuth();

	const [loading, setLoading] = useState<boolean>(false);

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
		<header className="w-full flex items-center justify-between h-[60px] px-4">
			<Link to="/">
				<div className="flex items-center">
					<h1 className="text-2xl font-bold text-primary-text">Tasky</h1>
				</div>
			</Link>
			<div className="flex items-center">
				<div className="flex items-center gap-2">
					<div
						style={{ backgroundColor: user?.user_color }}
						className="w-8 h-8 rounded-full flex justify-center items-center font-bold"
					>
						{user?.user_name[0]}
					</div>
					<p className="ml-2 text-primary-text">{user?.user_name}</p>
					{user ? (
						<Button
							loading={loading}
							onClick={logout}
						>
							Log out
						</Button>
					) : (
						<Link to="/login">
							<Button
								onClick={() => {}}
								loading={loading}
							>
								Log in
							</Button>
						</Link>
					)}
				</div>
			</div>
		</header>
	);
};
