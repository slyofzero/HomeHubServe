import { IApiRes } from ".";

export interface IService {
  id: number;
  name: string;
  description: string;
  price: number;
}

export interface ServiceApiRes {
  message: string;
  data: IService[];
}
