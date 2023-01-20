/** @type {import('tailwindcss').Config} */
module.exports = {
	content: ["./src/components/**/*.{js,jsx,ts,tsx}", "./src/pages/**/*.{js,jsx,ts,tsx}"],
	theme: {
		extend: {
			colors: {
				primary: "#1E90FF",
				secondary: "#FF6347",
				danger: "#DC143C",
				dark: "#343A40",
				light: "#F8F9FA",
				white: "#FFFFFF",
			},
		},
	},
	plugins: [],
};
