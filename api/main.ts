import * as fs from 'fs';
import axios from 'axios';

const apiKey = 'a8b61f7af3c34ea0930c';
const serviceId = 'I2790';

(async () => {
  let hello: any[] = [];

  do {
    let offset = 1;
    let limit = 1000;
    const url = `http://openapi.foodsafetykorea.go.kr/api/${apiKey}/${serviceId}/json/${offset}/${
      offset + limit - 1
    }`;
    const result = await axios.get(url);
    hello = hello.concat(result.data['I2790'].row);
    console.log(`Current: ${hello.length}`);
    offset += limit;
  } while (hello.length < 90000);

  fs.promises.writeFile('dataset.json', JSON.stringify(hello));
})();
