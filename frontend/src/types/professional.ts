import { IService } from "./service";

export interface IProfessional {
  created_on: number;
  description: string;
  experience: number;
  id: number;
  name: string;
  pincode: number;
  price: number;
  rating: number;
  service_id: number;
  service_name: string;
  status: "REJECTED" | "ACCEPTED" | "PENDING" | "BLOCKED";
  user_id: number;
  jobs_done: number;
}
export interface ProfessionalApiRes {
  message: string;
  data: IProfessional[];
  page: number;
  totalPages: number;
}

export interface ServiceProfessionalApiRes {
  message: string;
  data: {
    professionals: IProfessional[];
    service: IService;
  };
}
