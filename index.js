import { readFile, setData } from './readData.js';

const addData = async (name, age, description) => {
	try {
		const data = await readFile();

		let id = data.length > 0 ? data[data.length - 1].id + 1 : 1;

		data.push({ id, name: name, edad: age, description: description });

		let save = await setData(data);
		return save;
	} catch (error) {
		console.log(error);
	}
};

// addData('Lucas', 20, 'Avatar blanco');

const changeData = async (id, name, age, description) => {
	try {
		let data = await readFile();
		const iUpdate = data.find((u) => u.id === id);

		if (iUpdate) {
			iUpdate.id = id;
			iUpdate.name = name;
			iUpdate.age = age;
			iUpdate.description = description;

			let save = await setData(data);
			return save;
		}
	} catch (error) {
		console.log(error);
	}
};

changeData(5, 'Mateo', 18, 'Gato');
