import { Button } from '@greenhoodspace/ui/components/button';
import { Breadcrumb } from '../../../packages/ui/src/components/breadcrumb';

const Home = () => {
	return (
		<div className="flex flex-col flex-1 items-center justify-center bg-zinc-50 font-sans dark:bg-black gap-4">
			<h1 className="font-lora text-2xl">Home Page</h1>
			<Button className="font-sans text-md w-100">Just a Button</Button>
			<Breadcrumb />
		</div>
	);
};

export default Home;
