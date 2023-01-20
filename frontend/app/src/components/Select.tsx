import { FC, useCallback, useEffect, useRef, useState } from "react";
import { CheckIcon } from "./CheckIcon";
import { ArrowHeadIcon } from "./ArrowHeadIcon";

export const Select: FC<{
	defaultValue: any;
	onChange: (value: any) => void;
	options: { label: string; value: any }[];
}> = ({ onChange, options, defaultValue }) => {
	const [opened, setOpened] = useState<boolean>(false);
	const toggleDropdown = useCallback(() => {
		setOpened(!opened);
	}, [opened, setOpened]);

	const [value, setValue] = useState<any>(defaultValue);
	const [errors, setErrors] = useState<string[]>([]);

	const handleChange = (_data: string) => {
		setOpened(false);
		setValue(_data);
		onChange(_data);
	};

	useEffect(() => {
		if (!options.find((option) => option.value === value)) setValue(defaultValue);
	}, [options]);

	const dropdownRef = useRef<HTMLDivElement>(null);

	useEffect(() => {
		const onClickOut = (event: { target: any }) => {
			if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
				setOpened(false);
			}
		};

		document.addEventListener("mousedown", onClickOut);

		return () => {
			document.removeEventListener("mousedown", onClickOut);
		};
	}, [dropdownRef]);

	console.log(options.find((option) => option.value === value));

	return (
		<>
			<div className="relative">
				<div
					onClick={toggleDropdown}
					className={`p-2 text-sm border rounded-md cursor-pointer flex items-center gap-1 w-max ${
						opened ? "border-secondary-text" : "border-primary-text/20"
					} bg-secondary-bg`}
				>
					<span>{options.find((option) => option.value === value)?.label}</span>
					<ArrowHeadIcon className="w-4 h-4 fill-primary-text" />
				</div>
				<div
					ref={dropdownRef}
					className="absolute left-0 z-10 overflow-hidden transition-all top-11"
					style={{ height: !opened ? "0" : `${options.length * 28 + 18}px` }}
				>
					<div className="flex flex-col items-center gap-2 border rounded-md w-max bg-secondary-bg border-primary-text/20">
						<ul className="flex flex-col items-start p-2">
							{options.map((option) => (
								<li
									onClick={() => handleChange(option.value)}
									key={option.value}
									className="w-full px-2 py-1 text-sm rounded-md cursor-pointer hover:bg-info text-primary-text/80"
								>
									<span className="flex items-center gap-2">
										{option.label}
										{value === option.value && (
											<CheckIcon className="w-3 h-3 fill-primary-text/80" />
										)}
									</span>
								</li>
							))}
						</ul>
					</div>
				</div>
			</div>
		</>
	);
};
