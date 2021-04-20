//This is the webcam interface. It defines what is expected of each webcam object
export interface Webcam {
		id: number;
		name: string;
		area: string; // Which forecast area: EH, WH etc.
		country: string; //Scotland, England, Wales
		webpage: string;
		imgurl: string;
		updated: Date;
}
