import fs from 'fs';

const readFile = async () => {
	try {
		if (fs.existsSync('data.json')) {
			const data = await fs.promises.readFile('data.json', 'utf-8');
			return await JSON.parse(data);
		} else {
			return [];
		}
	} catch (error) {
		console.log(error);
		return [];
	}
};

const setData = async (data) => {
	try {
		await fs.promises.writeFile('data.json', JSON.stringify(data, null, '\t'));
	} catch (error) {
		console.log(error);
	}
};

export { readFile, setData };
