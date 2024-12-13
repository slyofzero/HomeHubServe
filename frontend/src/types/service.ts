export interface IService {
  id: number;
  name: string;
  description: string;
  pay_per_h: number;
}

export interface ServiceApiRes {
  message: string;
  data: IService[];
}
