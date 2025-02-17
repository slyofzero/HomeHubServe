export interface IService {
  id: number;
  name: string;
  description: string;
  base_price: number;
}

export interface ServiceApiRes {
  message: string;
  data: IService[];
}
