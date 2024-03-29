import { FC } from "react";

export const Spinner: FC<{ className?: string }> = ({ className }) => {
	return (
		<>
			<svg
				className={`${className ?? ""}`}
				version="1.1"
				id="L4"
				xmlns="http://www.w3.org/2000/svg"
				xmlnsXlink="http://www.w3.org/1999/xlink"
				viewBox="0 0 52 90"
				xmlSpace="preserve"
			>
				<circle
					stroke="none"
					cx="6"
					cy="50"
					r="6"
				>
					<animate
						attributeName="opacity"
						dur="1s"
						values="0;1;0"
						repeatCount="indefinite"
						begin="0.1"
					/>
				</circle>
				<circle
					stroke="none"
					cx="26"
					cy="50"
					r="6"
				>
					<animate
						attributeName="opacity"
						dur="1s"
						values="0;1;0"
						repeatCount="indefinite"
						begin="0.2"
					/>
				</circle>
				<circle
					stroke="none"
					cx="46"
					cy="50"
					r="6"
				>
					<animate
						attributeName="opacity"
						dur="1s"
						values="0;1;0"
						repeatCount="indefinite"
						begin="0.3"
					/>
				</circle>
			</svg>
		</>
	);
};
