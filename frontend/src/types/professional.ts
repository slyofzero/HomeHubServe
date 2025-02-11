export interface IProfessional {
  created_on: number;
  description: string;
  experience: number;
  id: number;
  name: string;
  pincode: number;
  rating: number;
  service_name: string;
  status: "REJECTED" | "ACCEPTED" | "PENDING" | "BLOCKED";
  user_id: number;
}

export interface ProfessionalApiRes {
  message: string;
  data: IProfessional[];
}
