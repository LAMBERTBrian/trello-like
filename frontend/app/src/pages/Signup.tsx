import React, { useCallback } from "react";
import { Button } from "../components/Button";

export const Signup = () => {
	const [name, setName] = React.useState<string>("");
	const [email, setEmail] = React.useState<string>("");
	const [password, setPassword] = React.useState<string>("");

	const [loading, setLoading] = React.useState<boolean>(false);

	const signup = useCallback(async () => {
		setLoading(true);

		const res = await (
			await fetch("http://localhost:5000/auth/signup", {
				method: "POST",
				headers: {
					"Content-Type": "application/json",
				},
				body: JSON.stringify({
					email,
					name,
					password,
				}),
			})
		).json();

		const { user, session_token } = res.data as {
			user: {
				user_id: number;
				user_name: string;
				user_email: string;
			};
			session_token: string;
		};

		setLoading(false);

		console.log(user, session_token);

		if (user && session_token) {
			localStorage.setItem("session_token", session_token);
			// get redirect to home page
			window.location.href = "/";
		}
	}, [email, password]);

	return (
		<div className="flex justify-center items-center w-full h-screen flex-col gap-8">
			<h1 className="text-5xl font-bold">Sign up</h1>
			<div className="bg-secondary-bg flex-col gap-3 rounded-lg flex justify-center items-center p-6">
				<input
					onChange={(e) => {
						setName(e.target.value);
					}}
					className="bg-tertiary-bg text-sm rounded-md px-2"
					type="text"
					placeholder="Username"
				/>
				<input
					onChange={(e) => {
						setEmail(e.target.value);
					}}
					className="bg-tertiary-bg text-sm rounded-md px-2"
					type="email"
					placeholder="Email"
				/>
				<input
					onChange={(e) => {
						setPassword(e.target.value);
					}}
					className="bg-tertiary-bg text-sm rounded-md px-2"
					type="password"
					placeholder="Password"
				/>
				<Button
					onClick={signup}
					loading={loading}
				>
					Sign up
				</Button>
			</div>
		</div>
	);
};
