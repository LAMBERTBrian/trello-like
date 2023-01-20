import ReactDOM from "react-dom/client";
import "./index.css";
import { RouterProvider, createBrowserRouter } from "react-router-dom";
import { Home } from "./pages/Home";
import { Login } from "./pages/Login";
import { Signup } from "./pages/Signup";
import { Dashboard } from "./pages/Dashboard";

const router = createBrowserRouter([
	{
		path: "/",
		element: <Home />,
	},
	{
		path: "/login",
		element: <Login />,
	},
	{
		path: "/signup",
		element: <Signup />,
	},
	{
		path: "/dashboard",
		element: <Dashboard />,
	},
]);

ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(
	<RouterProvider router={router} />
);
