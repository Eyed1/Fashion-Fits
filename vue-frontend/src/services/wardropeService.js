import axios from 'axios';

const baseUrl = 'http://localhost:3001/api/wardrope';

class WardropeService {
  clothes = [
    { id: 1, type: 'shirt', color: 'red', category: 'top', imgLink: 'https://i5.walmartimages.com/asr/77ec8a2d-c570-40c0-a937-4043cbe1dd1f.9c92151c510cd452b2b8f7693c11ebd3.jpeg'},
    { id: 2, type: 'polo', color: 'blue', category: 'top', imgLink: 'https://www.shoppeaches.com/cdn/shop/products/little-english-light-blue-polo_1000x.jpg?v=1582216625'},
    { id: 3, type: 'pants', color: 'green', category: 'bottom', imgLink: 'https://www.net-a-porter.com/variants/images/42247633208803705/in/w2000_q60.jpg'},
    { id: 4, type: 'coat', color: 'yellow', category: 'outerwear', imgLink: 'https://www.acornonline.com/graphics/products/large/XE6402_front.jpg'},
  ];

  async getWardrope() {
    return this.clothes; 
  }

  async getFits() {
    const response = await axios.get(`${baseUrl}/fits`);
    return response.data;
  }

  async addClothe(clothe) {
    const response = await axios.post(baseUrl, clothe);
    return response.data;
  }

  async removeClothe(clothe) {
    const response = await axios.delete(`${baseUrl}/${clothe.id}`);
    return response.data;
  }

  async editClothe(clothe) {
    const response = await axios.put(`${baseUrl}/${clothe.id}`, clothe);
    return response.data;
  }
}

/*
class WardropeService {
  async getWardrope() {
    const response = await axios.get(baseUrl);
    return response.data;
  }

  async getFits() {
    const response = await axios.get(`${baseUrl}/fits`);
    return response.data;
  }

  async addClothe(clothe) {
    const response = await axios.post(baseUrl, clothe);
    return response.data;
  }

  async removeClothe(clothe) {
    const response = await axios.delete(`${baseUrl}/${clothe.id}`);
    return response.data;
  }
}
*/

export { WardropeService };