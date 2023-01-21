import React, { useCallback, useEffect } from "react";
import { useAuth } from "../hooks/auth";
import { Spinner } from "../components/Spinner";
import { TrashIcon } from "../components/TrashIcon";
import { ArrowHeadIcon } from "../components/ArrowHeadIcon";
import { Button } from "../components/Button";
import { PencilIcon } from "../components/PencilIcon";
import { CheckIcon } from "../components/CheckIcon";
import { Select } from "../components/Select";
import { Header } from "../components/Header";
import { CrossIcon } from "../components/CrossIcon";

export const Dashboard = () => {
	const [user] = useAuth();

	const [loading, setLoading] = React.useState<boolean>(false);

	const [lists, setLists] = React.useState<
		{
			list_id: number;
			list_title: string;
			tasks: {
				task_id: number;
				task_title: string;
				user_id: string;
				user_name: string;
				user_color: string;
			}[];
		}[]
	>([]);

	const [users, setUsers] = React.useState<
		{
			user_id: string;
			user_name: string;
			user_email: string;
			user_color: string;
		}[]
	>([]);

	const [editMode, setEditMode] = React.useState<number | null>(null);
	const [createMode, setCreateMode] = React.useState<number | null>(null);

	const [newAsignee, setNewAsignee] = React.useState<string | null>(null);

	const [newTaskName, setNewTaskName] = React.useState<string | null>(null);
	const [newTaskAsignee, setNewTaskAsignee] = React.useState<string | null>(null);

	const [listCreateMode, setListCreateMode] = React.useState<boolean>(false);
	const [newListName, setNewListName] = React.useState<string | null>(null);

	useEffect(() => {
		setNewAsignee(null);
	}, [editMode]);

	const fetchLists = async () => {
		setLoading(true);

		const res = await (
			await fetch("http://localhost:5000/lists", {
				method: "POST",
				headers: {
					"Content-Type": "application/json",
				},
				body: JSON.stringify({
					session_token: localStorage.getItem("session_token"),
				}),
			})
		).json();

		setLists(res.data.lists);

		setLoading(false);

		console.log(res);

		return res;
	};

	const fetchUsers = async () => {
		setLoading(true);

		const res = await (
			await fetch("http://localhost:5000/users", {
				method: "POST",
				headers: {
					"Content-Type": "application/json",
				},
				body: JSON.stringify({
					session_token: localStorage.getItem("session_token"),
				}),
			})
		).json();

		setUsers(res.data.users);

		setLoading(false);

		console.log(res);

		return res;
	};

	const deleteTask = async (task_id: number) => {
		setLoading(true);

		const res = await (
			await fetch("http://localhost:5000/tasks", {
				method: "DELETE",
				headers: {
					"Content-Type": "application/json",
				},
				body: JSON.stringify({
					session_token: localStorage.getItem("session_token"),
					task_id,
				}),
			})
		).json();

		await fetchLists();

		setLoading(false);

		console.log(res);

		return res;
	};

	const deleteList = async (list_id: number) => {
		setLoading(true);

		const res = await (
			await fetch("http://localhost:5000/lists", {
				method: "DELETE",
				headers: {
					"Content-Type": "application/json",
				},
				body: JSON.stringify({
					session_token: localStorage.getItem("session_token"),
					list_id,
				}),
			})
		).json();

		await fetchLists();

		setLoading(false);

		console.log(res);

		return res;
	};

	const createList = async () => {
		setLoading(true);

		const res = await (
			await fetch("http://localhost:5000/lists/create", {
				method: "POST",
				headers: {
					"Content-Type": "application/json",
				},
				body: JSON.stringify({
					session_token: localStorage.getItem("session_token"),
					list_title: newListName,
				}),
			})
		).json();

		await fetchLists();

		setLoading(false);

		console.log(res);

		return res;
	};

	const changeAssignee = async (task_id: number, user_id: string) => {
		setLoading(true);

		const res = await (
			await fetch("http://localhost:5000/tasks/assign", {
				method: "PUT",
				headers: {
					"Content-Type": "application/json",
				},
				body: JSON.stringify({
					session_token: localStorage.getItem("session_token"),
					task_id,
					user_id,
				}),
			})
		).json();

		await fetchLists();

		setLoading(false);

		console.log(res);

		return res;
	};

	const createTask = async (list_id: number) => {
		setLoading(true);

		setCreateMode(null);

		const res = await (
			await fetch("http://localhost:5000/tasks/create", {
				method: "POST",

				headers: {
					"Content-Type": "application/json",
				},

				body: JSON.stringify({
					session_token: localStorage.getItem("session_token"),
					list_id,
					task_name: newTaskName,
					user_id: newTaskAsignee,
				}),
			})
		).json();

		await fetchLists();

		setLoading(false);

		console.log(res);

		return res;
	};

	const moveTask = async (task_id: number, list_id: number) => {
		setEditMode(null);

		setLoading(true);

		const res = await (
			await fetch("http://localhost:5000/tasks/move", {
				method: "PUT",
				headers: {
					"Content-Type": "application/json",
				},
				body: JSON.stringify({
					session_token: localStorage.getItem("session_token"),
					task_id,
					list_id,
				}),
			})
		).json();

		await fetchLists();

		setLoading(false);

		console.log(res);

		return res;
	};

	React.useEffect(() => {
		if (!user) return;

		fetchLists();
		fetchUsers();
	}, [user]);

	useEffect(() => {
		setNewTaskAsignee(users[0]?.user_id ?? null);
	}, [users]);

	const handleEditModeClick = useCallback(
		(task: {
			task_id: number;
			task_title: string;
			user_id: string;
			user_name: string;
			user_color: string;
		}) => {
			if (editMode && newAsignee) {
				changeAssignee(task.task_id, newAsignee);
			}

			setEditMode(editMode === task.task_id ? null : task.task_id);
		},
		[editMode, newAsignee]
	);
	return (
		<div className="flex-col w-full min-h-screen flex items-center">
			<Header />
			{user && lists ? (
				<div className={`flex gap-12 h-screen w-full p-12 overflow-x-scroll flex-nowrap`}>
					{lists.map((list, i) => (
						<div className="flex flex-col gap-4 min-w-[250px]">
							<div className="flex justify-between pb-2 border-secondary-text border-b font-semibold items-center">
								<h1 className="text-left ">{list.list_title}</h1>
								{!(i == 0 && i == lists.length - 1) && (
									<button
										disabled={loading}
										onClick={() => deleteList(list.list_id)}
									>
										<TrashIcon className="fill-gradient-1 w-4 h-4" />
									</button>
								)}
							</div>
							{list.tasks.map((task) => (
								<div
									key={task.task_id}
									className="w-full bg-secondary-bg rounded-lg p-3 flex flex-col gap-4 justify-between items-center relative"
								>
									<div className="w-full justify-between flex items-center">
										<div className="flex items-center justify-between">
											<span className="font-bold text-left">{task.task_title}</span>
										</div>
										<div className="flex items-center gap-1">
											<button
												disabled={loading}
												onClick={() => handleEditModeClick(task)}
												className="mr-1"
											>
												{editMode ? (
													<CheckIcon className="fill-gradient-1 w-4 h-4" />
												) : (
													<PencilIcon className="fill-gradient-1 w-4 h-4" />
												)}
											</button>
											<button
												disabled={loading}
												onClick={() => deleteTask(task.task_id)}
											>
												<TrashIcon className="fill-gradient-1 w-4 h-4" />
											</button>
											<button
												disabled={i === 0}
												onClick={() => {
													moveTask(task.task_id, lists[i - 1].list_id);
												}}
											>
												<ArrowHeadIcon className="fill-gradient-1 w-4 h-4 rotate-90" />
											</button>
											<button
												disabled={i === lists.length - 1}
												onClick={() => {
													moveTask(task.task_id, lists[i + 1].list_id);
												}}
											>
												<ArrowHeadIcon className="fill-gradient-1 w-4 h-4 transform -rotate-90" />
											</button>
										</div>
									</div>
									{/* Profile picture being the first letter of the task.user_name and random color */}
									<div className="w-full flex flex-col gap-3 items-start">
										<div className="flex gap-4 items-center">
											<div
												className={`w-8 h-8 rounded-full flex justify-center items-center text-white font-bold`}
												style={{
													backgroundColor:
														newAsignee && editMode === task.task_id && users
															? users.find((user) => user.user_id === newAsignee)?.user_color
															: task.user_color,
												}}
											>
												{newAsignee && editMode === task.task_id && users
													? users.find((user) => user.user_id === newAsignee)?.user_name[0]
													: task.user_name[0]}
											</div>
											{editMode === task.task_id && users && (
												<Select
													options={users.map((user) => ({
														label: user.user_name,
														value: user.user_id,
													}))}
													onChange={(value: any) => setNewAsignee(value)}
													defaultValue={task.user_id}
												/>
											)}
										</div>
									</div>
								</div>
							))}
							<div>
								{createMode === list.list_id ? (
									<div className="flex flex-col gap-3 p-3 bg-secondary-bg rounded-lg">
										<input
											type="text"
											className="w-full rounded-md focus:outline-none bg-tertiary-bg px-1 py-1 text-sm"
											placeholder="Task name"
											onChange={(e) => setNewTaskName(e.target.value)}
										/>
										<div className="flex gap-4 items-center">
											<div
												className={`w-8 h-8 rounded-full flex justify-center items-center text-white font-bold`}
												style={{
													backgroundColor: users
														? users.find((user) => user.user_id === newTaskAsignee)?.user_color
														: "#000000",
												}}
											>
												{users
													? users.find((user) => user.user_id === newTaskAsignee)?.user_name[0]
													: "A"}
											</div>
											<Select
												options={users.map((user) => ({
													label: user.user_name,
													value: user.user_id,
												}))}
												onChange={(value: any) => setNewTaskAsignee(value)}
												defaultValue={users[0].user_id}
											/>
										</div>
										<div className="w-full flex gap-3">
											<Button
												loading={loading}
												disabled={loading || !newTaskName || !newTaskAsignee}
												onClick={() => createTask(list.list_id)}
											>
												Confirm
											</Button>
											<Button
												loading={loading}
												disabled={loading}
												onClick={() => setCreateMode(null)}
											>
												<CrossIcon className="w-4 h-4 fill-primary-text" />
											</Button>
										</div>
									</div>
								) : (
									<Button
										onClick={() => setCreateMode(list.list_id)}
										disabled={loading}
										loading={loading}
									>
										New Task
									</Button>
								)}
							</div>
						</div>
					))}
					<div className="flex flex-col w-full items-start gap-3">
						{listCreateMode ? (
							<div className="flex flex-col gap-3 p-3 bg-secondary-bg rounded-lg">
								<input
									type="text"
									className="w-full rounded-md focus:outline-none bg-tertiary-bg px-1 py-1 text-sm"
									placeholder="List name"
									onChange={(e) => setNewListName(e.target.value)}
								/>
								<div className="w-full flex gap-3">
									<Button
										loading={loading}
										disabled={loading || !newListName}
										onClick={createList}
									>
										Confirm
									</Button>
									<Button
										loading={loading}
										disabled={loading}
										onClick={() => setListCreateMode(false)}
									>
										<CrossIcon className="w-4 h-4 fill-primary-text" />
									</Button>
								</div>
							</div>
						) : (
							<Button
								onClick={() => setListCreateMode(true)}
								disabled={loading}
								loading={loading}
							>
								New List
							</Button>
						)}
					</div>
					{Array(Math.max(0, 5 - lists.length))
						.fill(0)
						.map((_, i) => (
							<div></div>
						))}
				</div>
			) : (
				<div className="flex flex-col flex-auto gap-4 justify-center items-center">
					<Spinner className="fill-primary-text w-12 h-12" />
				</div>
			)}
		</div>
	);
};
