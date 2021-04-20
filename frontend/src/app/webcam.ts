//This is the webcam interface. It defines what is expected of each webcam object
export interface Webcam {
		id: number;
		country: string; //Scotland, England, Wales
		area: string; // Which forecast area: EH, WH etc.
		name: string;
		url: string;
		lastupdated: Date;
}
