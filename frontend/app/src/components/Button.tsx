import { Spinner } from "./Spinner";

export interface ButtonProps {
	children: React.ReactNode;
	onClick: React.MouseEventHandler<HTMLButtonElement>;
	solid?: boolean;
	disabled?: boolean;
	loading?: boolean;
}

export const Button = ({ children, onClick, disabled = false, loading = false }: ButtonProps) => {
	return (
		<button
			className={`bg-gradient-to-r text-sm from-gradient-1 flex justify-center items-center disabled:opacity-80 transition-all duration-150 to-gradient-2 rounded-md outline-none px-6 text-primary-text h-[40px] py-1 `}
			onClick={onClick}
			disabled={disabled || loading}
		>
			{loading ? <Spinner className="fill-primary-text w-5 h-5" /> : children}
		</button>
	);
};
