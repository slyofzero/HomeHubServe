export interface IUser {
  address: string;
  email: string;
  id: number;
  joined_on: number;
  name: string;
  pincode: number;
  role: "ADMIN" | "REG_PROFESSIONAL" | "PROFESSIONAL" | "CUSTOMER";
  status: "BLOCKED" | "ALLOWED";
}

export interface UsersApiRes {
  message: string;
  data: IUser[];
}

export interface SingleUserApiRes {
  message: string;
  data: IUser;
}
