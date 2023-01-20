/** @type {import('tailwindcss').Config} */
module.exports = {
	content: ["./src/**/*.{js,jsx,ts,tsx}"],
	theme: {
		extend: {
			colors: {
				"primary-bg": "#10122A",
				"secondary-bg": "#161936",
				"tertiary-bg": "#222561",
				"primary-text": "#FFFFFF",
				"secondary-text": "#404155",
				"gradient-1": "#455EB5",
				"gradient-2": "#673FD7",
			},
		},
	},
	plugins: [],
};
